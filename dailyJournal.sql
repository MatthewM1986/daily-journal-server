CREATE TABLE `Entry` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `concept` TEXT NOT NULL,
    `entry` TEXT NOT NULL,
    `date` INTEGER NOT NULL,
    `mood_id` INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
);
INSERT INTO `Entry`
VALUES (null, "1235", "123", 1598458543321, 1);
INSERT INTO `Entry`
VALUES (null, "abc", "123", 1598458548239, 2);
INSERT INTO `Entry`
VALUES (null, "Delete", "Now Deleting", 1598458559152, 1);
INSERT INTO `Entry`
VALUES (null, "ANGRY", "jlj", 1598557358781, 3);
INSERT INTO `Entry`
VALUES (null, "678", "Now Deleting", 1598557373697, 4);
CREATE TABLE `Mood` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL
);
INSERT INTO `Mood`
VALUES (null, "Happy");
INSERT INTO `Mood`
VALUES (null, "Sad");
INSERT INTO `Mood`
VALUES (null, "Angry");
INSERT INTO `Mood`
VALUES (null, "Ok");