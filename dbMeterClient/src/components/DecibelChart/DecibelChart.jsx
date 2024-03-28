import { useEffect, useRef, useState } from "react";
import Chart from "chart.js/auto";
import PropTypes from "prop-types";

function DecibelChart({ sensorData }) {
  const [data, setData] = useState([]);
  const chartRef = useRef(null);

  useEffect(() => {
    if (sensorData && sensorData.timeStamp && sensorData.dbLevel) {
      // Combine new sensor data with existing data array
      const newData = [
        ...data,
        { timeStamp: sensorData.timeStamp, dbLevel: sensorData.dbLevel },
      ];
      setData(newData);
    }
  }, [sensorData]);

  useEffect(() => {
    if (data.length > 0) {
      const timestamps = data.map((entry) =>
        new Date(entry.timeStamp).toLocaleTimeString()
      );
      const dbLevels = data.map((entry) => entry.dbLevel);

      const ctx = chartRef.current.getContext("2d");

      new Chart(ctx, {
        type: "line",
        data: {
          labels: timestamps,
          datasets: [
            {
              label: "Decibel Level",
              data: dbLevels,
              borderColor: "blue",
              backgroundColor: "rgba(0, 0, 255, 0.1)",
              borderWidth: 1,
            },
          ],
        },
        options: {
          responsive: true,
          scales: {
            x: {
              type: "time",
              time: {
                displayFormats: {
                  hour: "MMM D, HH:mm",
                },
              },
              title: {
                display: true,
                text: "Time",
              },
            },
            y: {
              title: {
                display: true,
                text: "Decibel Level",
              },
            },
          },
        },
      });
    }
  }, [data]);

  return (
    <div className="decibel-chart">
      <h3>Chart Here</h3>
      <canvas ref={chartRef}></canvas>
    </div>
  );
}

DecibelChart.propTypes = {
  sensorData: PropTypes.object,
};

export default DecibelChart;
