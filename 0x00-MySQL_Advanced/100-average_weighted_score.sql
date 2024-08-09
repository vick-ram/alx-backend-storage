-- Script that creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for student
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
	DECLARE weighted_sum INT DEFAULT 0;
	DECLARE total_weight INT DEFAULT 0;

	SELECT SUM(c.score * p.weight) INTO weighted_sum
	FROM corrections c
	INNER JOIN projects p ON c.project_id = p.id
	WHERE c.user_id = user_id;

	SELECT SUM(p.weight) INTO total_weight
	FROM corrections c
	INNER JOIN projects p ON c.project_id = p.id
	WHERE c.user_id = user_id;

	IF total_weight = 0 THEN
		UPDATE users
		SET average_score = 0
		WHERE id = user_id;
	ELSE
		UPDATE users
		SET average_score = weighted_sum / total_weight
		WHERE id = user_id;
	END IF;
END $$
DELIMITER ;
