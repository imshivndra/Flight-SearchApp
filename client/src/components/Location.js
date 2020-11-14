import React, { useState } from "react";
import { Form, Input, Button } from "antd";
import { DatePicker } from "antd";
import axios from "axios";
import FlightDetails from "./FlightDetails";

export default function Location() {
  const [flightData, setFlightData] = useState(null);

  const [form] = Form.useForm();
  const formLayout = "inline";
  const searchFlight = (values) => {
    axios
      .post("http://localhost:8000/flight/search-flight", {
        departure_city: values.departure,
        departure_time: Math.floor(Date.parse(values.date) / 1000),
        arrival_city: values.arrival,
      })
      .then((data) => {
        console.log("data", data);
        setFlightData(data.data);
      })
      .catch((err) => {
        console.log(err);
      });
  };

  return (
    <>
      <div>
        <Form
          layout={formLayout}
          form={form}
          initialValues={{
            layout: formLayout,
          }}
          onFinish={searchFlight}
        >
          <Form.Item name="departure">
            <Input placeholder="Departure City" required="true" />
          </Form.Item>
          <Form.Item name="arrival">
            <Input placeholder="Arrival City" required="true" />
          </Form.Item>
          <Form.Item name="date">
            <DatePicker showTime="true" format="h:mm a" />
          </Form.Item>

          <Form.Item>
            <Button type="primary" htmlType="submit">
              Search
            </Button>
          </Form.Item>
        </Form>
      </div>

      <div className="flight-data">
        {flightData == null ? null : flightData.length == 0 ? (
          <div>
            <h3>No Flight Found</h3>
          </div>
        ) : (
          flightData.map((flight_detail) => {
            return <FlightDetails data={flight_detail} />;
          })
        )}
      </div>
    </>
  );
}
