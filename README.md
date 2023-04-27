This modul is about Course Management System (CMS). It defines several models that describe different aspects of a course management system such as departments, programs, program lines, courses, course prerequisites, course offerings, semesters, and semester sessions.

Here's a brief overview of the functionality of each model:

    CMSDepartment: This model represents a department in the CMS. It has a name and can have many programs offered.

    CMSProgram: This model represents a program offered by a department. It has a name, duration, eligibility, and belongs to a department. It can have many program lines and program offerings.

    CMSProgramLine: This model represents a program line within a program. It has a name, semester, course, and belongs to a program. It can have many courses.

    CMSProgramOffered: This model represents a program offering within a program. It has a course code, name, credits hours, and belongs to a program and semester. It can have many program offering lines.

    CMSSemester: This model represents a semester within the CMS. It has a name and can have many program offerings.

    CMSProgramOfferLine: This model represents a program offering line within a program offering. It has a name, duration, semester, course, and belongs to a program offering. It can have many courses.
