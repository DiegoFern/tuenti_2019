
get_open_sub_query = ''' select date_time open,
                            user_id from activity

                                where action ='open' '''

get_close_q =''' select date_time close, 
                            user_id from activity
                            where  action='close'
                            '''
next_action ='''select A.date_time,A.user_id,A.action,min(B.date_time)
                    from activity A join activity B on  A.user_id=B.user_id 
                    where A.date_time<B.date_time  
                        group by A.user_id,A.date_time
'''

get_all_q = ''' select u.user_id ,t.open  ,min( u.close) 
                FROM ({op}) t join ({cl}) u on t.User_id=u.User_id
                    where t.open<u.close
                group by u.user_id,t.open
        '''.format(
                op=get_open_sub_query,
                cl=get_close_q,
                )

extrapole_close_open='''
select * from (
select 
    A.user_id,
    A.action,
    GREATEST(
        COALESCE(max(CASE WHEN B.date_time<=A.date_time
            and B.Action='open'
            THEN B.date_time
            ELSE NULL END
        ),NULL,min(B.date_time))  ,

        COALESCE(max(CASE WHEN B.date_time<A.date_time
            and B.Action='close'
            THEN B.date_time
            ELSE NULL END
        ),NULL,min(B.date_time)) 
        
    ) open,
   LEAST(
       COALESCE(min(CASE WHEN B.date_time>A.date_time
            and B.Action='open'
            THEN B.date_time
            ELSE NULL END
        ),NULL,max(B.date_time))  ,

        COALESCE(min(CASE WHEN B.date_time>=A.date_time
            and B.Action='close'
            THEN B.date_time
            ELSE NULL END
        ),NULL,
       max(B.date_time) )
    )  close 

from activity A join activity B on A.user_id=B.user_id
group by A.user_id,A.action,A.date_time) d
where A.action in ('close','open')
'''

I='''SELECT 
 user_id,
  open session_from ,close session_to ,
  sum(  1 ) num_actions ,
  TIMESTAMPDIFF(second,open,close) time 
  
FROM ({}) t
group by user_id,open,close
order by user_id,session_from
'''.format(
extrapole_close_open)
#--------------------------------

STATES = '''

select SUM(
CASE WHEN 
(b.date_time<a.date_time and (b.action='open' or b.action='close')) 
or (b.date_time=a.date_time and b.action='open')
THEN 1
ELSE 0
END

) State,
a.user_id,a.action,a.date_time 

from  activity a join activity b on a.user_id=b.user_id 
group by a.user_id,a.action,a.date_time
'''
DUPS='''select user_id,date_time,action,count(*) duplication
from activity group by user_id,date_time,action'''
J='''
SELECT STATES.user_id,
MIN(STATES.date_time) session_from ,
MAX(STATES.date_time) session_to ,
  -TIMESTAMPDIFF(second,MAX(STATES.date_time),MIN(STATES.date_time)) seconds ,
sum(DUPS.duplication) num_actions
FROM ({} ) STATES join ({}) DUPS on STATES.user_id = DUPS.user_id 

where  STATES.date_time = DUPS.date_time and STATES.action = DUPS.action 
GROUP BY user_id,state
order by user_id,session_from
'''.format(STATES,DUPS)
print(J,end=';')
