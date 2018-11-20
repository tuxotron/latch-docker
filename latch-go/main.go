package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

type Latch struct {
	Latched    bool   `json:"latched"`
	LastUpdate string `json:"lastUpdate"`
}

func handler(w http.ResponseWriter, r *http.Request) {

	jsonFile, err := os.Open("/usr/share/latch/latch-info.json")
	defer jsonFile.Close()

	var file []byte
	if err != nil {
		file, _ = ioutil.ReadFile("templates/nostatus.html")
	} else {
		byteValue, _ := ioutil.ReadAll(jsonFile)
		var latch Latch
		json.Unmarshal(byteValue, &latch)

		fmt.Println(latch)

		if latch.Latched {
			file, _ = ioutil.ReadFile("templates/webDown.html")
		} else {
			file, _ = ioutil.ReadFile("templates/webUp.html")
		}
	}

	fmt.Fprintf(w, string(file))
}

func main() {
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(":8081", nil))
}
