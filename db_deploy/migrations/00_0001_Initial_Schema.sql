-- Initial Schema 
-- Andrew Gentile
-- 2020-01-27

DROP TABLE IF EXISTS "countries";
CREATE TABLE "countries" (
    id INTEGER PRIMARY KEY,

    name TEXT UNIQUE NOT NULL,

    createdAt TIMESTAMP DEFAULT NOW(),
    updatedAt TIMESTAMP DEFAULT NOW()
);

DROP TABLE IF EXISTS "cities";
CREATE TABLE "cities" (
    id UUID PRIMARY KEY,

    name TEXT UNIQUE NOT NULL,

    countryId INTEGER NOT NULL,

    createdAt TIMESTAMP DEFAULT NOW(),
    updatedAt TIMESTAMP DEFAULT NOW()
);

DROP TABLE IF EXISTS "companies";
CREATE TABLE "companies" (
    id UUID PRIMARY KEY,

    name TEXT NOT NULL,

    countryId INTEGER NOT NULL,
    cityId INTEGER NOT NULL,

    createdAt TIMESTAMP DEFAULT NOW(),
    updatedAt TIMESTAMP DEFAULT NOW()
);

DROP TABLE IF EXISTS "sponsorships";
CREATE TABLE "sponsorships" (
    id UUID PRIMARY KEY,

    countryId INTEGER NOT NULL,
    cityId UUID NOT NULL,
    companyId UUID NOT NULL,

    type TEXT,
    route TEXT,
    
    createdAt TIMESTAMP DEFAULT NOW(),
    updatedAT TIMESTAMP DEFAULT NOW()
);
