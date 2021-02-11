CREATE OR REPLACE FUNCTION trg_sponsorships_before_update()
	RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
	-- Calculate MD5 hash of sponsorship fields
    NEW."hash" = MD5 (
     	CONCAT (
        	NEW."countryId",
          	NEW."cityId",
          	NEW."companyId",
          	NEW."type",
          	NEW."route"
     	)
     );
     
     RETURN NEW;
END $$;

DROP TRIGGER IF EXISTS "trg_sponsorships_before_update" ON "sponsorships";
CREATE TRIGGER "trg_sponsorships_before_update"
	BEFORE UPDATE
    ON "sponsorships"
    FOR EACH ROW
    EXECUTE PROCEDURE trg_sponsorships_before_update();
