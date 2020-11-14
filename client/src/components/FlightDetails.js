import React from "react";
export default function FlightDetails(props) {
  let data = props.data;
  let dateObj1 = new Date(data.departure_time * 1000);
  let departure_time = dateObj1.toLocaleTimeString("en-US", {
    hour: "numeric",
    hour12: true,
    minute: "numeric",
  });
  let dateObj2 = new Date(data.arrival_time * 1000);
  let arrival_time = dateObj2.toLocaleTimeString("en-US", {
    hour: "numeric",
    hour12: true,
    minute: "numeric",
  });

  return (
    <div className="flight-details">
      <div className="flight-box">
        <p>Flight Number</p>
        <h3>{data.number}</h3>
      </div>
      <div className="flight-box">
        <p>From</p>
        <h3>{data.departure_city + "-" + departure_time}</h3>
      </div>{" "}
      <div className="flight-box">
        <p>To</p>
        <h3>{data.arrival_city + "-" + arrival_time}</h3>
      </div>
    </div>
  );
}
