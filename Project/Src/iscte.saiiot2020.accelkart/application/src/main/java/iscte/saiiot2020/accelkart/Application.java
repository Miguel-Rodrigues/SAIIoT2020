package iscte.saiiot2020.accelkart;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import lombok.extern.slf4j.Slf4j;

@Slf4j
@SpringBootApplication
@EnableConfigurationProperties(SettingsProperties.class)
public class Application implements CommandLineRunner {

	@Autowired
	private SettingsProperties properties;

	public static void main(String[] args) {
		log.info("STARTING THE APPLICATION");
		SpringApplication.run(Application.class, args);
		log.info("APPLICATION FINISHED");
	}

	@Override
	public void run(String... args) {
		log.info("EXECUTING : command line runner");

		System.out.println("=============================================\n\n");

		System.out.println("Hello World");

		for (int i = 0; i < args.length; ++i) {
			log.info("args[{}]: {}", i, args[i]);
		}

		System.out.println(properties.getProp1());
		System.out.println(properties.getProp2());
		System.out.println(properties.getProp3());


		System.out.println("\n\n=============================================");
	}
}
