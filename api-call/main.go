package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"time"
)

type Response struct {
	Status string `json:"status"`
	Data   []struct {
		iD             int    `json:"id"`
		EmployeeName   string `json:"employee_name"`
		EmployeeSalary int    `json:"employee_salary"`
		EmployeeAge    int    `json:"employee_age"`
		ProfileImage   string `json:"profile_image"`
	} `json:"data"`
	Message string `json:"message"`
}

func main() {
	resp, err := http.Get("https://dummy.restapiexample.com/api/v1/employees")

	if err != nil {
		fmt.Printf("some error occured %s", err)
	}

	status := resp.StatusCode
	fmt.Println(status)

	for status != 200 {
		time.Sleep(2 * time.Second)
		fmt.Println("aryan mangla")
		res, _ := http.Get("https://dummy.restapiexample.com/api/v1/employees")
		status = res.StatusCode
		fmt.Println(status)
		resp = res
	}

	fmt.Println(status)

	defer resp.Body.Close()
	body, _ := ioutil.ReadAll(resp.Body)

	var result Response
	if err := json.Unmarshal(body, &result); err != nil {
		fmt.Println("Can not unmarshal JSON")
	}

	var sum = 0

	for _, rec := range result.Data {
		sum += int(rec.EmployeeSalary)
	}
	fmt.Println(sum)
}
