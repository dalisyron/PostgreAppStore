DROP TRIGGER if EXISTS check_price_not_negative on "Payments";
DROP FUNCTION  if EXISTS fun_check_price_not_negative;

CREATE FUNCTION fun_check_price_not_negative() RETURNS TRIGGER AS $$
BEGIN
	if (NEW.price <= 0) THEN
		raise exception 'Price must be positive';
	END IF;
END
$$
LANGUAGE plpgsql;

CREATE TRIGGER check_price_not_negative
  BEFORE INSERT OR UPDATE
  ON "Payments"
  FOR EACH ROW
  EXECUTE PROCEDURE fun_check_price_not_negative();
