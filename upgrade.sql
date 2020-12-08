BEGIN;

-- Running upgrade effc607b0530 -> 892d847df712

ALTER TABLE "Bug" ALTER COLUMN who SET NOT NULL;

UPDATE alembic_version SET version_num='892d847df712' WHERE alembic_version.version_num = 'effc607b0530';

COMMIT;

