-- IMPORTANT notices about this SQL file
-- Eana Eltu SQL data by Tobias Jaeggi (Tuiq, tuiq@clonk2c.ch), Richard Littauer (Taronyu, richard@learnnavi.org) and others is licensed under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License ( http://creativecommons.org/licenses/by-nc-sa/3.0/ ).
-- The full license text is available at http://creativecommons.org/licenses/by-nc-sa/3.0/legalcode .

-- localized table.
CREATE TABLE IF NOT EXISTS `localizedWords` (`id` int(11) NOT NULL,`languageCode` char(5) NOT NULL,`localized` text NULL,`partOfSpeech` varchar(100) NULL, UNIQUE KEY `idlc` (`id`,`languageCode`)) DEFAULT CHARSET=utf8;
-- meta table.
CREATE TABLE IF NOT EXISTS `metaWords` (`id` int(11) NOT NULL, `navi` varchar(100) NOT NULL,`ipa` varchar(100) NOT NULL,`infixes` varchar(100) NULL,`partOfSpeech` varchar(100) NOT NULL,PRIMARY KEY (`id`)) DEFAULT CHARSET=utf8;
-- TRUNCATE ACTION!
TRUNCATE TABLE `metaWords`;
TRUNCATE TABLE `localizedWords`;
-- INSERT MASSACRE