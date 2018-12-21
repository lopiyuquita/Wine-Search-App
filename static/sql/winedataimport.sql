CREATE TABLE IF NOT EXISTS `wine`.`country` (
  `country_id` INT(11) NOT NULL AUTO_INCREMENT,
  `country_name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`country_id`)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci


CREATE TABLE IF NOT EXISTS `wine`.`province` (
  `province_id` INT(11) NOT NULL AUTO_INCREMENT,
  `province_name` VARCHAR(45) NULL DEFAULT NULL,
  `country_id` INT(11) NOT NULL,
  PRIMARY KEY (`province_id`),
  INDEX `fk_province_countries1_idx` (`country_id` ASC) VISIBLE,
  CONSTRAINT `fk_province_countries1`
    FOREIGN KEY (`country_id`)
    REFERENCES `wine`.`country` (`country_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci


CREATE TABLE IF NOT EXISTS `wine`.`region1` (
  `region1_id` INT(11) NOT NULL,
  `region1_name` VARCHAR(45) NULL DEFAULT NULL,
  `province_id` INT(11) NOT NULL,
  PRIMARY KEY (`region1_id`),
  INDEX `fk_region_1_province1_idx` (`province_id` ASC) VISIBLE,
  CONSTRAINT `fk_region_1_province1`
    FOREIGN KEY (`province_id`)
    REFERENCES `wine`.`province` (`province_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci


CREATE TABLE IF NOT EXISTS `wine`.`region2` (
  `region2_id` INT(11) NOT NULL,
  `region2_name` VARCHAR(45) NULL DEFAULT NULL,
  `region1_id` INT(11) NOT NULL,
  PRIMARY KEY (`region2_id`),
  INDEX `fk_region_2_region_11_idx` (`region1_id` ASC) VISIBLE,
  CONSTRAINT `fk_region_2_region_11`
    FOREIGN KEY (`region1_id`)
    REFERENCES `wine`.`region1` (`region1_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci


CREATE TABLE IF NOT EXISTS `wine`.`variety` (
  `variety_id` INT(11) NOT NULL,
  `variety_name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`variety_id`)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci


CREATE TABLE IF NOT EXISTS `wine`.`variety_region1` (
  `region1_id` INT(11) NOT NULL,
  `variety_id` INT(11) NOT NULL,
  `variety_region1_id` INT(11) NOT NULL,
  PRIMARY KEY (`variety_region1_id`),
  INDEX `fk_region_1_has_varieties_region_11_idx` (`region1_id` ASC) VISIBLE,
  INDEX `fk_region_1_has_varieties_varieties1_idx` (`variety_id` ASC) VISIBLE,
  CONSTRAINT `fk_region_1_has_varieties_region_11`
    FOREIGN KEY (`region1_id`)
    REFERENCES `wine`.`region1` (`region1_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_region_1_has_varieties_varieties1`
    FOREIGN KEY (`variety_id`)
    REFERENCES `wine`.`variety` (`variety_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci


CREATE TABLE IF NOT EXISTS `wine`.`variety_region2` (
  `variety_id` INT(11) NOT NULL,
  `region2_id` INT(11) NOT NULL,
  `variety_region2_id` INT(11) NOT NULL,
  INDEX `fk_varieties_has_region_2_region_21_idx` (`region2_id` ASC) VISIBLE,
  INDEX `fk_varieties_has_region_2_varieties1_idx` (`variety_id` ASC) VISIBLE,
  PRIMARY KEY (`variety_region2_id`),
  CONSTRAINT `fk_varieties_has_region_2_varieties1`
    FOREIGN KEY (`variety_id`)
    REFERENCES `wine`.`variety` (`variety_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_varieties_has_region_2_region_21`
    FOREIGN KEY (`region2_id`)
    REFERENCES `wine`.`region2` (`region2_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci


CREATE TABLE IF NOT EXISTS `wine`.`taster` (
  `taster_id` INT(11) NOT NULL,
  `taster_name` VARCHAR(45) NULL DEFAULT NULL,
  `twitter_handles` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`taster_id`)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci


CREATE TABLE IF NOT EXISTS `wine`.`winery` (
  `winery_id` INT(11) NOT NULL,
  `winery_name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`winery_id`)
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci


CREATE TABLE IF NOT EXISTS `wine`.`winery_variety` (
  `variety_id` INT(11) NOT NULL,
  `winery_id` INT(11) NOT NULL,
  `winery_variety_id` INT(11) NOT NULL,
  INDEX `fk_varieties_has_wineries_wineries1_idx` (`winery_id` ASC) VISIBLE,
  INDEX `fk_varieties_has_wineries_varieties1_idx` (`variety_id` ASC) VISIBLE,
  PRIMARY KEY (`winery_variety_id`),
  CONSTRAINT `fk_varieties_has_wineries_varieties1`
    FOREIGN KEY (`variety_id`)
    REFERENCES `wine`.`variety` (`variety_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_varieties_has_wineries_wineries1`
    FOREIGN KEY (`winery_id`)
    REFERENCES `wine`.`winery` (`winery_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci


CREATE TABLE IF NOT EXISTS `wine`.`wine_taster` (
  `taster_id` INT(11) NOT NULL,
  `wine_id` INT(11) NOT NULL,
  `points` INT(11) NULL,
  `wine_taster_id` INT(11) NOT NULL,
  INDEX `fk_tasters_has_wines_wines1_idx` (`wine_id` ASC) VISIBLE,
  INDEX `fk_tasters_has_wines_tasters1_idx` (`taster_id` ASC) VISIBLE,
  PRIMARY KEY (`wine_taster_id`),
  CONSTRAINT `fk_tasters_has_wines_tasters1`
    FOREIGN KEY (`taster_id`)
    REFERENCES `wine`.`taster` (`taster_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_tasters_has_wines_wines1`
    FOREIGN KEY (`wine_id`)
    REFERENCES `wine`.`wine` (`wine_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci


CREATE TABLE IF NOT EXISTS `wine`.`wine` (
  `wine_id` INT(11) NOT NULL AUTO_INCREMENT,
  `wine` VARCHAR(45) NOT NULL,
  `description` VARCHAR(255) NULL DEFAULT NULL,
  `designation` VARCHAR(45) NULL DEFAULT NULL,
  `price` INT(11) NULL DEFAULT NULL,
  `winery_id` INT(11) NOT NULL,
  `country_id` INT(11) NOT NULL,
  `province_id` INT(11) NOT NULL,
  `region1_id` INT(11) NOT NULL,
  `region2_id` INT(11) NOT NULL,
  `variety_id` INT(11) NOT NULL,
  PRIMARY KEY (`wine_id`),
  INDEX `fk_wines_wineries1_idx` (`winery_id` ASC) VISIBLE,
  INDEX `fk_wines_countries1_idx` (`country_id` ASC) VISIBLE,
  INDEX `fk_wines_province1_idx` (`province_id` ASC) VISIBLE,
  INDEX `fk_wines_region_11_idx` (`region1_id` ASC) VISIBLE,
  INDEX `fk_wines_region_21_idx` (`region2_id` ASC) VISIBLE,
  INDEX `fk_wines_varieties1_idx` (`variety_id` ASC) VISIBLE,
  CONSTRAINT `fk_wines_wineries1`
    FOREIGN KEY (`winery_id`)
    REFERENCES `wine`.`winery` (`winery_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_wines_countries1`
    FOREIGN KEY (`country_id`)
    REFERENCES `wine`.`country` (`country_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_wines_province1`
    FOREIGN KEY (`province_id`)
    REFERENCES `wine`.`province` (`province_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_wines_region_11`
    FOREIGN KEY (`region1_id`)
    REFERENCES `wine`.`region1` (`region1_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_wines_region_21`
    FOREIGN KEY (`region2_id`)
    REFERENCES `wine`.`region2` (`region2_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_wines_varieties1`
    FOREIGN KEY (`variety_id`)
    REFERENCES `wine`.`variety` (`variety_id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci
