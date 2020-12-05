package iscte.saiiot2020.accelkart;

import org.springframework.boot.context.properties.ConfigurationProperties;

import lombok.Getter;
import lombok.Setter;

/**
 * Configuration
 */


 @ConfigurationProperties(prefix="settings")
public class SettingsProperties
 {
    @Getter @Setter private String prop1 = "None";

    @Getter @Setter private int prop2 = 10;

    @Getter @Setter private float prop3 = 20;
}