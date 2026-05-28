from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `student` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(32) NOT NULL COMMENT '学生姓名',
    `age` INT NOT NULL COMMENT '学生年龄',
    `major` VARCHAR(32) NOT NULL COMMENT '学生专业'
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """


MODELS_STATE = (
    "eJztlm1vmzAQx79KxKtW6qYEyEP7Lo00bdOWSm03TWoqZLABL8amttlaVfnusw0EQhJKpG"
    "lppb3h4e5v++6nO45nK2EQEfH+RmYQUWld9J4tChKkHpqus54F0rRyaIMEPjFaURP5QnIQ"
    "6L1CQARSJohEwHEqMaPKSjNCtJEFSohpVJkyih8y5EkWIRkjrhx398qMKUSPSJSv6dILMS"
    "JwI1gM9dnG7smn1Ng+UfnBCPVpvhcwkiW0EqdPMmZ0rcZ5+BGiiAOJ9PaSZzp8HV2RaJlR"
    "HmklyUOsrYEoBBmRtXQ7MggY1fxUNMIkGOlT3tkDd+xOnJE7URITydoyXuXpVbnnCw2B+a"
    "21Mn4gQa4wGCtu5r5FbhYDvhtdqW/AUyE34ZWo2uiVhgpfVTKt/KxFNvRHo0U2Hg5C9XwO"
    "HXV1+3nAL1NNwKNHEI1krF4duwXh9+n17OP0+sSxT/XeTJV2XvLzwmMbl6ZcUQXRDqh7y7"
    "FQv1yP/xQpGruL7DycuB2R/pVCrX19wE/GD6nM9YLXVZouGjjmCo5XmvqrGS5r/a8NPgiW"
    "vwGH3paH2WyfdtuV2EnTAqiqaFhkqOMvJskUcRzEu2ZM4WkdMaDS/J8wb2jC/EJc6JAOaO"
    "XakiM3c3eKG21rD4cd+lap9jau8TWGimqNAyAW8rcJcNDvdwCoVHsBGt8mQHWiLH5SNyF+"
    "vrma74ZYW9IA+Y2qBO8gDuRZj2Ah718n1haKOmsddCLEA6nDO/k6/dHkOvtydWkoMCEjbn"
    "YxG1wee7ys/gCD/wsM"
)
