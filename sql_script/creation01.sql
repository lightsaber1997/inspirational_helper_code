CREATE TABLE `user` (
	`id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`loginId` varchar(50) NOT NULL,
	`encryptedPassword` varchar(512) NOT NULL,
	`email` varchar(256),
	`phoneNumber` varchar(64),
	`authority` varchar(20) NOT NULL,
	`userNameInApp` varchar(56),
    `realName` varchar(56),
    `createdAt` timestamp DEFAULT CURRENT_TIMESTAMP,
    `updatedAt` timestamp DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;



CREATE TABLE `korea_sigudong` (
	`id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`si` varchar(50) NOT NULL,
	`gu` varchar(512) NOT NULL,
	`dong` varchar(256),
    `createdAt` timestamp DEFAULT CURRENT_TIMESTAMP,
    `updatedAt` timestamp DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

select * from korea_sigudong
where si like "제주%";



CREATE TABLE `grade` (
	`id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`gradeCategory1` varchar(32),
    `gradeCategory2` varchar(32),
    `createdAt` timestamp DEFAULT CURRENT_TIMESTAMP,
    `updatedAt` timestamp DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `student_profile` (
	`id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`studentId` int NOT NULL,
	`content` text NOT NULL,
    `createdAt` timestamp DEFAULT CURRENT_TIMESTAMP,
    `updatedAt` timestamp DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;


CREATE TABLE `subject` (
	`id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
	`subjectName` varchar(50) NOT NULL,
    `createdAt` timestamp DEFAULT CURRENT_TIMESTAMP,
    `updatedAt` timestamp DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

insert into `subject`
(`subjectName`)
values
("국어"),
("수학"),
("영어"),
("과학"),
("사회"),
("컴퓨터"),
("미술"),
("체육"),
("기타");
