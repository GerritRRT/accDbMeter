import PropTypes from "prop-types";
import { useState, useEffect } from "react";
import "./summary.scss";

function Summary({ dbLevel }) {
  //   const formattedDB = Math.round(dbLevel);

  const [dbLevels, setDbLevels] = useState([]);
  const [minLevel, setMinLevel] = useState(null);
  const [maxLevel, setMaxLevel] = useState(null);
  const [averageLevel, setAverageLevel] = useState(null);

  const calculateAverage = (array) => {
    const sum = array.reduce((acc, val) => acc + val, 0);
    return sum / array.length;
  };

  // Update min, max, average, and median levels whenever dbLevels changes
  useEffect(() => {
    if (dbLevels.length > 0) {
      setMinLevel(Math.min(...dbLevels));
      setMaxLevel(Math.max(...dbLevels));
      setAverageLevel(calculateAverage(dbLevels));
    }
  }, [dbLevels]);

  const handleDbLevelReceived = (level) => {
    setDbLevels((prevLevels) => [...prevLevels, level]);
  };

  useEffect(() => {
    const intervalId = setInterval(() => {
      handleDbLevelReceived(dbLevel);
    }, 1000); // Simulating receiving level every second

    return () => clearInterval(intervalId);
  }, [dbLevel]); // Run only once on component mount

  return (
    <div className="summary">
      <div className="summary-item">
        <p>Minimum</p>
        <p>{Math.round(minLevel)}</p>
      </div>
      <div className="summary-item">
        <p>Average</p>
        <p>{Math.round(averageLevel)}</p>
      </div>
      <div className="summary-item">
        <p>Maximum</p>
        <p>{Math.round(maxLevel)}</p>
      </div>
    </div>
  );
}

Summary.propTypes = {
  dbLevel: PropTypes.number,
};

export default Summary;
