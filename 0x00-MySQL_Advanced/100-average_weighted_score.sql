-- Script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for student
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight INT;

    SELECT SUM(c.score * p.weight)
    INTO total_weighted_score
    FROM corrections c
    INNER JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    SELECT SUM(p.weight)
    INTO total_weight
    FROM corrections c
    INNER JOIN projects p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    UPDATE users
    SET average_score = total_weighted_score / total_weight
    WHERE id = user_id;

END $$

DELIMITER ;
