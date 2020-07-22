DROP TRIGGER IF EXISTS delete_failed_status_payment ON "Payments";

DROP FUNCTION IF EXISTS fun_delete_failed_status_payment;

CREATE FUNCTION fun_delete_failed_status_payment ()
    RETURNS TRIGGER
    AS $$
BEGIN
	IF (NEW.status = 'SUCCESS') THEN
		delete from "Payments" where purchase_id = NEW.purchase_id AND status = 'FAILURE';
	END IF;
END
$$
LANGUAGE plpgsql;

CREATE TRIGGER delete_failed_status_payment
    BEFORE INSERT ON "Payments"
    FOR EACH ROW
	EXECUTE PROCEDURE fun_delete_failed_status_payment ();
