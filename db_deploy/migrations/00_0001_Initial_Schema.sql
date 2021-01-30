-- Initial Schema 
-- Andrew Gentile
-- 2020-01-27

DROP TABLE IF EXISTS "countries";
CREATE TABLE "countries" (
    "id" SERIAL PRIMARY KEY,

    "name" TEXT UNIQUE NOT NULL,
    "code3" TEXT UNIQUE NOT NULL,

    "createdAt" TIMESTAMP DEFAULT NOW(),
    "updatedAt" TIMESTAMP DEFAULT NOW()
);

DROP TABLE IF EXISTS "cities";
CREATE TABLE "cities" (
    "id" UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    "name" TEXT UNIQUE NOT NULL,

    "countryId" INTEGER NOT NULL REFERENCES "countries" ("id"),

    "createdAt" TIMESTAMP DEFAULT NOW(),
    "updatedAt" TIMESTAMP DEFAULT NOW()
);
CREATE UNIQUE INDEX ON "cities" ("name", "countryId");

DROP TABLE IF EXISTS "companies";
CREATE TABLE "companies" (
    "id" UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    "name" TEXT NOT NULL,

    "countryId" INTEGER NOT NULL REFERENCES "countries" ("id"),
    "cityId" UUID NOT NULL REFERENCES "cities" ("id"),

    "createdAt" TIMESTAMP DEFAULT NOW(),
    "updatedAt" TIMESTAMP DEFAULT NOW()
);
CREATE UNIQUE INDEX ON"companies" ("name", "countryId", "cityId");

DROP TABLE IF EXISTS "sponsorships";
CREATE TABLE "sponsorships" (
    "id" UUID PRIMARY KEY DEFAULT gen_random_uuid(),

    "countryId" INTEGER NOT NULL REFERENCES "countries" ("id"),
    "cityId" UUID NOT NULL REFERENCES "cities" ("id"),
    "companyId" UUID NOT NULL REFERENCES "companies" ("id"),

    "type" TEXT,
    "route" TEXT,
    
    "createdAt" TIMESTAMP DEFAULT NOW(),
    "updatedAT" TIMESTAMP DEFAULT NOW()
);
CREATE UNIQUE INDEX ON "sponsorships" ("companyId", "type");
