INSERT INTO academia.students (name, email) VALUES
('Ana', 'ana@example.com'),
('Juan', 'juan@example.com'),
('Valen', 'valen@example.com');

INSERT INTO academia.teachers (name, email) VALUES
('Carlos', 'carlos@universidad.com'),
('Laura', 'laura@universidad.com');


INSERT INTO academia.courses (name, credits, teacher_id) VALUES
('Cloud Computing', 3, 1),
('Internet of Things', 4, 2);

INSERT INTO academia.enrollments (student_id, course_id) VALUES
(1, 1),
(2, 1),
(3, 2);
