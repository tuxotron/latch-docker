package com.cyberhades.latch;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

import java.io.File;
import java.io.IOException;

@SpringBootApplication
@Controller
public class LatchApplication {

    public static void main(String[] args) {
        SpringApplication.run(LatchApplication.class, args);
    }


    @GetMapping("/")
    public String latchProtectedMethod() {

        final String LATCH_INFO_PATH = "/usr/share/latch/latch-info.json";

        final ObjectMapper mapper = new ObjectMapper();

        try {
            Latch latch = mapper.readValue(new File(LATCH_INFO_PATH), Latch.class);

            System.out.println(latch);

            if (latch.isLatched()) {
                return "webDown";
            } else {
                return "webUp";
            }


        } catch (IOException e) {
            return "nostatus";
        }

    }

}
