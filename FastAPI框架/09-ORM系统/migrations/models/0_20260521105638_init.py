from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `clas` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '班级名称'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '学生姓名',
    `pwd` VARCHAR(32) NOT NULL COMMENT '密码',
    `sno` INT NOT NULL COMMENT '学号',
    `clas_id` INT NOT NULL,
    CONSTRAINT `fk_student_clas_4be9b492` FOREIGN KEY (`clas_id`) REFERENCES `clas` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `teacher` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '教师姓名',
    `pwd` VARCHAR(32) NOT NULL COMMENT '密码',
    `tno` INT NOT NULL COMMENT '教师编号'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `course` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '课程名称',
    `teacher_id` INT NOT NULL COMMENT '课程老师',
    CONSTRAINT `fk_course_teacher_2de38fe7` FOREIGN KEY (`teacher_id`) REFERENCES `teacher` (`id`) ON DELETE CASCADE
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `student_course` (
    `student_id` INT NOT NULL,
    `course_id` INT NOT NULL,
    FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE,
    FOREIGN KEY (`course_id`) REFERENCES `course` (`id`) ON DELETE CASCADE,
    UNIQUE KEY `uidx_student_cou_student_0d222b` (`student_id`, `course_id`)
) CHARACTER SET utf8mb4 COMMENT='学生选课表';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztWW1vmzAQ/isVnzqpm8gLCdm3NFu1rmsrtd00qa2QA4agEDsFszaq+O+zDcSGACNNl9"
    "AqX/Jyd7bvHp/vHsyzMsMW9IJPIw8EyueDZwWBGaQ/MvKjAwXM50LKBASMPW5ophbjgPjA"
    "JFRmAy+AVGTBwPTdOXExolIUeh4TYpMausgRohC5DyE0CHYgmUCfKm7vqdhFFnyCQfp3Pj"
    "VsF3pWxk3XYmtzuUEWcy47ReSEG7LVxoaJvXCGhPF8QSYYLa1dRJjUgQj6gEA2PfFD5j7z"
    "LokyjSj2VJjELkpjLGiD0CNSuDUxMDFi+FFv4n1w2Cof261uv6t3el2dmnBPlpJ+FIcnYo"
    "8HcgQubpSI6wEBsQWHUeDGv1eQG02AXwxdap8Dj7qcBy+Fqgq9VCDgEylTiZ9yF/Y70KKf"
    "EPTvQq2rst8DW1XqoToDT4YHkUMm9G+nXQHhr+HV6Nvw6rDT/sDmxjS143y/SDRtrooilp"
    "r2VAKZCcbAnD4C3zIyGgF/QEILMqdWtuA4GXlydgU9wMNehT05nNfxLFvdgdoZHKUplEqT"
    "Q8IBw21chtiqatae5SUAAYd7zdZmK6XlCod+AAsLWaypLmXCZl/M9sVsC8VMH9uQFjCgjp"
    "tRzI6kbCQQmDSBjbWyMjvo39m5TYB1VW1RmKGq1wT4FdJ2pTus4LsK7gn2oeugM7jgGJ9S"
    "pwAyizI2qW03Yqa3gm1Zd6BiHzwua2Mun2joNGBI4vM9vB4Nv3xVovKGu2GrqdOvzwFa3G"
    "D2WXOzNmjaL6zTdKu0ca9Ht0pr2XfhQFUH6ebpem/zDeOBGbl+K4XpMyIDraWFaLM29vlG"
    "TOFCQjnZ7OU2Jdp4WKIkEx+HzkQeJaYtTBMqN/J9MaokE2kIBWxCiq6cTgSS0Z5P7PnEFk"
    "qyfM61gdWJWUUz+MT8sSAdy0FNzJuAqckw1dVWM3AMEF7jWCfWu2dicWpqHbu/PfYlw8bu"
    "qdbjstKIHcO31cpYQVnTu74N+Wp6qdg8/OrSUik1dsZJJRq1GSMVVyPvmZCKKPN8NEPus4"
    "w0wznzhDRLVzdnpBzeakqaPukVUFLpIbCckkrPnHtK2rTC+z4paU/TBvHNwJ6SvldKStai"
    "pKQplFROzb7d2jo9fdGro7ipbPjm6OUtv2kXhv/1ddIQ+q45Keq2iaay2QJhs++1b6jX/o"
    "F+kJyeup1BGrLj7lAfxUxPaGtajaZArUq7Atdl2wI7GmuAmJi/TQBbqloDQGpVCiDX5e4s"
    "MCLJDXIWxO/XlxcllxZiSA7In4gGeGu5Jjk68NyA3DcT1goUWdTM6VkQPHgyeIfnw995XE"
    "c/Lo85Cjggjs9n4RMcr9d4X7+9RH8B6oX9aw=="
)
