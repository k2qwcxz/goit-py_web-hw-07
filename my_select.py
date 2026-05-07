from sqlalchemy import func, desc
from conf.db import session
from conf.models import Student, Grade, Subject, Teacher, Group


def select_1():
    """1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""
    return (
        session.query(Student.fullname, func.avg(Grade.grade).label("avg_grade"))
        .join(Grade, Student.id == Grade.student_id)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(5)
        .all()
    )


def select_2(subject_id: int):
    """2. Знайти студента із найвищим середнім балом з певного предмета."""
    return (
        session.query(Student.fullname, func.avg(Grade.grade).label("avg_grade"))
        .join(Grade, Student.id == Grade.student_id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .first()
    )


def select_3(subject_id: int):
    """3. Знайти середній бал у групах з певного предмета."""
    return (
        session.query(Group.name, func.avg(Grade.grade).label("avg_grade"))
        .join(Student, Group.id == Student.group_id)
        .join(Grade, Student.id == Grade.student_id)
        .filter(Grade.subject_id == subject_id)
        .group_by(Group.id)
        .all()
    )


def select_4():
    """4. Знайти середній бал на потоці (по всій таблиці оцінок)."""
    return session.query(func.avg(Grade.grade).label("avg_grade")).scalar()


def select_5(teacher_id: int):
    """5. Знайти які курси читає певний викладач."""
    return (
        session.query(Subject.name)
        .filter(Subject.teacher_id == teacher_id)
        .all()
    )


def select_6(group_id: int):
    """6. Знайти список студентів у певній групі."""
    return (
        session.query(Student.fullname)
        .filter(Student.group_id == group_id)
        .all()
    )


def select_7(group_id: int, subject_id: int):
    """7. Знайти оцінки студентів у окремій групі з певного предмета."""
    return (
        session.query(Student.fullname, Grade.grade, Grade.grade_date)
        .join(Grade, Student.id == Grade.student_id)
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id)
        .all()
    )


def select_8(teacher_id: int):
    """8. Знайти середній бал, який ставить певний викладач зі своїх предметів."""
    return (
        session.query(func.avg(Grade.grade).label("avg_grade"))
        .join(Subject, Grade.subject_id == Subject.id)
        .filter(Subject.teacher_id == teacher_id)
        .scalar()
    )


def select_9(student_id: int):
    """9. Знайти список курсів, які відвідує певний студент."""
    return (
        session.query(Subject.name)
        .join(Grade, Subject.id == Grade.subject_id)
        .filter(Grade.student_id == student_id)
        .distinct()
        .all()
    )


def select_10(student_id: int, teacher_id: int):
    """10. Список курсів, які певному студенту читає певний викладач."""
    return (
        session.query(Subject.name)
        .join(Grade, Subject.id == Grade.subject_id)
        .filter(
            Grade.student_id == student_id,
            Subject.teacher_id == teacher_id
        )
        .distinct()
        .all()
    )


if __name__ == "__main__":
    print("1:", select_1())
    print("2:", select_2(1))
    print("3:", select_3(1))
    print("4:", select_4())
    print("5:", select_5(1))
    print("6:", select_6(1))
    print("7:", select_7(1, 1))
    print("8:", select_8(1))
    print("9:", select_9(1))
    print("10:", select_10(1, 1))