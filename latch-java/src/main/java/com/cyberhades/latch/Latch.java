package com.cyberhades.latch;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.databind.annotation.JsonDeserialize;
import com.fasterxml.jackson.databind.annotation.JsonSerialize;
import com.fasterxml.jackson.datatype.jsr310.deser.LocalDateTimeDeserializer;
import com.fasterxml.jackson.datatype.jsr310.ser.LocalDateTimeSerializer;

import java.time.LocalDateTime;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Latch {

    private boolean latched;
    private LocalDateTime lastUpdate;

    public boolean isLatched() {
        return latched;
    }

    public void setLatched(boolean latched) {
        this.latched = latched;
    }

    @JsonDeserialize(using = LocalDateTimeDeserializer.class)
    public LocalDateTime getLastUpdate() {
        return lastUpdate;
    }

    @JsonSerialize(using = LocalDateTimeSerializer.class)
    public void setLastUpdate(LocalDateTime lastUpdate) {
        this.lastUpdate = lastUpdate;
    }

    @Override
    public String toString() {
        return "Latch{" +
                "latched=" + latched +
                ", lastUpdated=" + lastUpdate +
                '}';
    }
}
