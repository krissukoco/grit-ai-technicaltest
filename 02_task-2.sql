-- INIT TABLES
CREATE TABLE lecturer_history (
  lecturer_name VARCHAR(10),
  term VARCHAR(20),
  activity VARCHAR(10)
);
CREATE TABLE master_term(
  term VARCHAR(20)
);

-- TEST DATA
INSERT INTO lecturer_history VALUES
('Yanuar', '2018 Semester 1', 'Active'),
('Yanuar', '2019 Semester 2', 'Leave'),
('Yanuar', '2020 Semester 1', 'Active'),
('Singgih', '2018 Semester 2', 'Active'),
('Singgih', '2019 Semester 2', 'Resigned');

INSERT INTO master_term VALUES
('2017 Semester 1'),
('2017 Semester 2'),
('2018 Semester 1'),
('2018 Semester 2'),
('2019 Semester 1'),
('2019 Semester 2'),
('2020 Semester 1'),
('2020 Semester 2'),
('2021 Semester 1');

-- ANSWER (Note: on PostgreSQL)
SELECT
    lh.lecturer_name,
    master_term.term,
    COALESCE(lh2.activity, '-') AS status
FROM (
    SELECT DISTINCT lecturer_name FROM lecturer_history
) AS lh
CROSS JOIN master_term
LEFT JOIN
(
    SELECT lecturer_name, SUBSTRING(term, 1, 4) as term_year, activity FROM lecturer_history
) AS lh2
ON lh.lecturer_name = lh2.lecturer_name AND lh2.term_year = SUBSTRING(master_term.term, 1, 4)
ORDER BY lh.lecturer_name DESC, master_term.term;