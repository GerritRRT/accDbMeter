import { NumberFormatter } from "../NumberFormatter/NumberFormatter";
import Comparables from "../Comparables/Comparables";
import Summary from "../Summary/Summary";
import DecibelChart from "../DecibelChart/DecibelChart.jsx";
import PropTypes from "prop-types";
import "./dbmeter.scss";

function Dbmeter({ sensorData }) {
  const { sensorId, dbLevel, sensorName, timestamp } = sensorData;
  const formattedDB = Math.round(dbLevel);
  const time = new Date(timestamp).toLocaleTimeString();

  return (
    <>
      <div className="meter">
        <div className="meter-top meter-segment">
          <div className="meter-top-header">
            <h1 className="meter-header-name">{sensorName}</h1>
            <div className="meter-top-header-subheader">
              <p>Sensor ID:{sensorId}</p>
              <p>{time}</p>
            </div>
          </div>
          <div className="meter-top-output">
            <div className="meter-top-output-color-ring">
              <div className="meter-top-output-screen">
                <div className="meter-top-output-screen-num">
                  <NumberFormatter number={formattedDB} />
                </div>
                <p className="meter-top-output-screen-backdrop">000</p>
              </div>
            </div>
          </div>
          {dbLevel && <Comparables decibel={formattedDB} />}
        </div>
        <div className="meter-middle meter-segment">
          <Summary dbLevel={dbLevel} />
        </div>
        <div className="meter-bottom meter-segment">
          <DecibelChart sensorData={sensorData} />
        </div>
      </div>
    </>
  );
}

Dbmeter.propTypes = {
  sensorData: PropTypes.object,
};

export default Dbmeter;
