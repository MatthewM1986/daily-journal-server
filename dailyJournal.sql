CREATE TABLE `Entries` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `concept` TEXT NOT NULL,
    `entry` TEXT NOT NULL,
    `date` INTEGER NOT NULL,
    `lmood_id` INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Mood`(`id`)
);
INSERT INTO `Entries`
VALUES (null, "1235", "123", 1598458543321, 1);
INSERT INTO `Entries`
VALUES (null, "abc", "123", 1598458548239, 2);
INSERT INTO `Entries`
VALUES (null, "Delete", "Now Deleting", 1598458559152, 1);
INSERT INTO `Entries`
VALUES (null, "ANGRY", "jlj", 1598557358781, 3);
INSERT INTO `Entries`
VALUES (null, "678", "Now Deleting", 1598557373697, 4);
CREATE TABLE `Moods` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL,
);
INSERT INTO `Moods`
VALUES (null, "Happy");
INSERT INTO `Moods`
VALUES (null, "Sad");
INSERT INTO `Moods`
VALUES (null, "Angry");
INSERT INTO `Moods`
VALUES (null, "Ok");