DROP TRIGGER if EXISTS check_game_name on "Games";
DROP FUNCTION if EXISTS fun_check_game_name;

CREATE FUNCTION fun_check_game_name() RETURNS TRIGGER AS $$
BEGIN
	if (NEW.display_name LIKE '%blood%') THEN
		raise exception 'Name cannot contain that word';
	END IF;
END
$$
LANGUAGE plpgsql;

CREATE TRIGGER check_game_name
  BEFORE INSERT
  ON "Games"
  FOR EACH ROW
  EXECUTE PROCEDURE fun_check_game_name();
