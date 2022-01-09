import psycopg2

def query1():
            con = psycopg2.connect(host = "localhost",database="cricket",user = "postgres",password = "1234")
            cur = con.cursor()
            cur.execute("Select COUNT(*) from player_stats where bowling_economy < 6;")
            rows = cur.fetchall()
            print("Number of players whose bowling economy is less than 6 is",rows[0][0])
            cur.close()
            con.close()
def query2():
            con = psycopg2.connect(host = "localhost",database="cricket",user = "postgres",password = "1234")
            cur = con.cursor()
            cur.execute("Select name from umpire where name like 'A%';")
            rows = cur.fetchall()
            print("Names are",rows[0][0],",",rows[1][0])
            cur.close()
            con.close()
def query3():
            con = psycopg2.connect(host = "localhost",database="cricket",user = "postgres",password = "1234")
            cur = con.cursor()
            cur.execute("Select * from players where jersey_no > 70 EXCEPT Select * from players where jersey_no in (75,80); ")
            rows = cur.fetchall()
            for r in rows:
                for c in r:
                     print(c,end = " ")
                print()
            
def query4():
            con = psycopg2.connect(host = "localhost",database="cricket",user = "postgres",password = "1234")
            cur = con.cursor()
            cur.execute("select player_name,country from players p, team_authority t,teams te where p.player_id = t.captain_id and p.team_id = te.team_id; ")
            rows = cur.fetchall()
            for r in rows:
                for c in r:
                     print(c,end = " ")
                print()
def query5():
            con = psycopg2.connect(host = "localhost",database="cricket",user = "postgres",password = "1234")
            cur = con.cursor()
            cur.execute("select p.player_id,player_name,team_id,runs,batting_strike_rate from players p, player_stats s where p.player_id = s.player_id order by runs desc;")
            rows = cur.fetchall()
            for r in rows:
                for c in r:
                     print(c,end = " ")
                print()
def query6():
            con = psycopg2.connect(host = "localhost",database="cricket",user = "postgres",password = "1234")
            cur = con.cursor()
            cur.execute("select match_id,name from match inner join ground on ground.ground_id = match.ground_id; ")
            rows = cur.fetchall()
            for r in rows:
                for c in r:
                     print(c,end = " ")
                print()
def query7():
            con = psycopg2.connect(host = "localhost",database="cricket",user = "postgres",password = "1234")
            cur = con.cursor()
            cur.execute("select player_name from players where player_id in ( select player_id from player_stats where bowling_economy >= (Select AVG(bowling_economy) from player_stats)); ")
            rows = cur.fetchall()
            for r in rows:
                for c in r:
                     print(c,end = " ")
                print()
def query8():
            con = psycopg2.connect(host = "localhost",database="cricket",user = "postgres",password = "1234")
            cur = con.cursor()
            cur.execute("select t.team_id,country,MAX(batting_strike_rate) from players p, player_stats ps,teams t where p.player_id = ps.player_id and t.team_id = p.team_id group by t.team_id order by team_id;")
            rows = cur.fetchall()
            for r in rows:
                for c in r:
                     print(c,end = " ")
                print()
def query9():
            con = psycopg2.connect(host = "localhost",database="cricket",user = "postgres",password = "1234")
            cur = con.cursor()
            cur.execute("select third_umpire,name,COUNT(third_umpire) from match_umpire inner join umpire on ump_id = third_umpire group by third_umpire,name;")
            rows = cur.fetchall()
            for r in rows:
                for c in r:
                     print(c,end = " ")
                print()
def query10():
            con = psycopg2.connect(host = "localhost",database="cricket",user = "postgres",password = "1234")
            cur = con.cursor()
            cur.execute("Select * from players p join player_stats s on p.player_id = s.player_id where wickets = 0; ")
            rows = cur.fetchall()
            for r in rows:
                for c in r:
                     print(c,end = " ")
                print()
def default():
           print("incorrect choice")

print("Select a query from 1 to 10")
i = int(input())
if i==1:
    query1()
elif i==2:
    query2()
elif i==3:
    query3()
elif i==4:
    query4()
elif i==5:
    query5()
elif i==6:
    query6()
elif i==7:
    query7()
elif i==8:
    query8()
elif i==9:
    query9()
elif i==10:
    query10()
else:
    default()


'''switcher = {
            1: query1,
            2: query2,
            3: query3,
            4: query4,
            5: query5,
            6: query6,
            7: query7,
            8: query8,
            9: query9,
            10: query10
            }

def switch(query):
    return switcher.get(query, default)





#close the cursor
cur.close()'''
