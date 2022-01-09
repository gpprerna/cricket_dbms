drop database cricket;
create database cricket;

\c cricket

Create table teams(team_id int primary key, country varchar(20) NOT NULL, jersey_color varchar(20) UNIQUE , board varchar(15) UNIQUE NOT NULL);

Create table ground(ground_id int primary key, name varchar(30) NOT NULL, location varchar(20), incharge_name varchar(20) NOT NULL);

Create table players(player_id int primary key, player_name varchar(20) NOT NULL, dob date, jersey_no int, team_id int, Foreign Key (team_id) references teams(team_id));

Create table coach(coach_id int primary key, name varchar(20) NOT NULL, dob date, nationality varchar(20), team_id int NOT NULL, since date NOT NULL);

Create table umpire(ump_id int primary key, name varchar(20) NOT NULL, dob date, nationality varchar(20));

Create table match(match_id int primary key,match_date date UNIQUE, team_one_id int, team_two_id int, result varchar(20), ground_id int NOT NULL, Foreign Key (team_one_id) references teams(team_id), Foreign Key (team_two_id) references teams(team_id), Foreign Key (ground_id) references ground(ground_id));

Create table match_umpire(match_id int primary key, onfield_umpire_one int NOT NULL,  onfield_umpire_two int, third_umpire int, Foreign Key (match_id) references match(match_id), Foreign key (onfield_umpire_one) references umpire(ump_id), Foreign key (onfield_umpire_two) references umpire(ump_id), Foreign key (third_umpire) references umpire(ump_id));

Create table team_authority(team_id int primary key, captain_id int UNIQUE, coach_id int UNIQUE, Foreign Key (team_id) references teams(team_id),Foreign Key (captain_id) references players(player_id),Foreign Key (coach_id) references coach(coach_id));

Create table player_stats(player_id int NOT NULL, 
runs int, 
wickets int , 
batting_strike_rate float, 
bowling_economy float,
Primary key(player_id),
Foreign key(player_id) references players(player_id));

