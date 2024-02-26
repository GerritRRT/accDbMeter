
def index(data = ""):
    html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="./style.css">
            <title>ACC DB Sensor | Login</title>
        </head>
            <body>
                <header>
                    <div class="wide">
                        <h1>ACC DB Meter | Sensor Config Login Page</h1>
                        <div class="config-header">
                            <p>v1.0</p>
                        </div>
                    </div>
                </header>
                <main>
                    <div class="login-form">
                        <form class="login" action="/login" method="post">
                            <p>{}</p>
                            <div class="form-item">
                                <label class="input-label" for="username">Username:</label>
                                <input type="text" name="username" id="username" placeholder="username">
                            </div>
                            <div class="form-item">
                                <label class="input-label" for="password">Password: </label>
                                <input type="password" name="password" id="password" placeholder="password">
                            </div>
                            <button class="button-submit" type="submit">Submit</button>
                        </form>
                    </div>


                </main>
                <footer>
                    <p>Created by the ACC Software Design Team 2024</p>
                </footer>
            </body>
        </html>
    """ .format(data)
    return html

def dashboard(data, args={}):
    """
    returns an html string that can be sent to the server.
    Data must be a dictionary with the following:
     - username
     - sensorAddress
     - mqttAddress
     - sensorName
     - sensorLocation
     - xLoc
     - yLoc
     - mqttPort
     - mqttUsername
     - mqttPassword
     - mqttRate
    """
    

    html = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link rel="stylesheet" href="./style.css">
            <title>ACC DB Sensor</title>
        </head>
            <body>
                <header>
                    <div class="wide">
                        <h1>ACC DB Meter Sensor</h1>
                        <div class="config-header">
                            <p>v1.0</p>
                            <p>logged in as: {username}</p>
                            <p>Sensor Address: {sensorAddress}</p>
                            <p>MQTT Address: {mqttAddress}</p>
                        </div>
                    </div>
                    <form action="/logout" method="post">
                        <button type="submit">Logout</button>
                    </form>
                </header>
                <main>
                    <div class="config-header">
                        <h1>DB Sensor Configuration</h1>
                        <a class="btn" href="/restart">Restart Sensor</a>
                        <a class="btn" href="/mqttStop">Stop MQTT</a>
                        <a class="btn" href="/mqttStart">Start MQTT</a>
                        <a class="btn" href="/mqttRestart">Restart MQTT</a>
                    </div>
                    <div class="form-container">
                        <form action="/update/sensordata" method="post" >
                            <h2>Device Information</h2>
                            <div class="form-item">
                                <label class="input-label" for="sensorName">Sensor Name</label>
                                <input class="text-input" type="text" name="sensorName" id="sensorName" value="{sensorName}">
                            </div>
                            <div class="form-item">
                                <label class="input-label" for="username">Username</label>
                                <input class="text-input" type="text" name="username" id="username" value="{username}">
                            </div>
                            <div class="form-item">
                                <label class="input-label" for="password">Password</label>
                                <input class="text-input" type="password" name="password" id="password" >
                            </div>
                            <div class="form-item">
                                <label class="input-label" for="confPassword">Confirm Password</label>
                                <input class="text-input" type="password" name="confPassword" id="confPassword" >
                            </div>
                            <div class="center">
                                <button class="button-submit" type="submit">Submit</button>
                            </div>
                        </form>
                            <div class="center">
                                <hr>
                            </div>
                            <h2>Physical Location</h2>
                        <form action="/update/sensorlocation" method="post">
                            <div class="form-item">
                                <label class="input-label tooltip" for="sensorLocation">Location Name
                                    <span class="tooltiptext">Provide a descriptive location for this sensor.</span>
                                </label>
                                <input class="text-input" type="text" name="sensorLocation" id="sensorLocation" value="{sensorLocation}">
                            </div>
                            <!-- <h3>Distance from left to right (X), and front to back (Y)</h3> -->
                            <div class="form-item">
                                <label class="input-label tooltip" for="units">Units
                                    <span class="tooltiptext">Select a measurement unit (english or metric)</span>
                                </label>
                                <select name="units" id="units">
                                    <option value="feet" selected>Feet</option>
                                    <option value="meters" >Meters</option>
                                </select>
                            </div>
                            <div class="form-item">
                                <label class="input-label tooltip" for="xLoc">X - Location
                                    <span class="tooltiptext">Distance left or right from center stage (left is negative)</span>
                                </label>
                                <input class="text-input" type="number" name="xLoc" id="xLoc" value="{xLoc}">
                            </div>
                            <div class="form-item">
                                <label class="input-label tooltip" for="yLoc">Y - Location
                                    <span class="tooltiptext">Distance from the front of the stage (onstage is negative)</span>
                                </label>
                                <input class="text-input" type="number" name="yLoc" id="yLoc" value="{yLoc}">
                            </div>
                            <div class="center">
                                <button class="button-submit" type="submit">Submit</button>
                            </div>
                        </form>
                            <div class="center">
                                <hr>
                            </div>
                            <h2>MQTT Server Settings</h2>
                        <form action="/update/mqttsettings" method="post">
                            <div class="form-item">
                                <label class="input-label tooltip" for="mqttAddress">MQTT Server 
                                    <span class="tooltiptext">Ip Address or Server Name (ie: 10.1.1.10, or hive.mq.com)</span>
                                </label>
                                
                                <input class="text-input" type="text" name="mqttAddress" id="mqttAddress" value="{mqttAddress}">
                            </div>
                            <div class="form-item">
                                <label class="input-label tooltip" for="mqttPort">MQTT Port 
                                    <span class="tooltiptext">Port Number for MQTT Server</span>
                                </label>
                                
                                <input class="text-input" type="text" name="mqttPort" id="mqttPort" value="{mqttPort}">
                            </div>
                            <div class="form-item">
                                <label class="input-label tooltip" for="mqttUsername">MQTT Username 
                                    <span class="tooltiptext">Your username for logging into the MQTT Server</span>
                                </label>
                                
                                <input class="text-input" type="text" name="mqttUsername" id="mqttUsername" value="{mqttUsername}">
                            </div>
                            <div class="form-item">
                                <label class="input-label tooltip" for="mqttPassword">MQTT Password 
                                    <span class="tooltiptext">Password for logging into MQTT Server.  WARNING THIS WILL BE SAVED UNHASHED IN THE CONFIG.JSON FILE</span>
                                </label>
                                
                                <input class="text-input" type="text" name="mqttPassword" id="mqttPassword">
                            </div>
                            <div class="form-item">
                                <label class="input-label tooltip" for="mqttRate">MQTT Msg Rate 
                                    <span class="tooltiptext">Select how many times per second to send messages</span>
                                </label>
                                
                                <select name="mqttRate" id="mqttRate">
                                    <option value="0" >Select an option</option>
                                    <option value=".016" >1 per min</option>
                                    <option value="1" >1hz</option>
                                    <option value="6" >10hz</option>
                                    <option value="30" >30hz</option>
                                    <option value="60" >60hz</option>
                                    <option value="600" >600hz</option>
                                    <option value="6000" >6000hz</option>
                                    <option value="20000" >20000hz</option>
                                    <option value="40000" >40000hz</option>
                                </select>
                            </div>
                            <div class="center">
                                <button class="button-submit" type="submit">Submit</button>
                            </div>
                        </form>
                        
                    </div>
                </main>
                <footer>
                    <p>Created by the ACC Software Design Team 2024</p>
                </footer>
            </body>
        </html>
    '''.format(
        username = data['username'],
        sensorAddress = data['sensorAddress'],
        mqttAddress = data['mqttAddress'],
        sensorName = data['sensorName'],
        sensorLocation = data['sensorLocation'],
        xLoc = data['xLoc'],
        yLoc = data['yLoc'], 
        mqttPort= data['mqttPort'],
        mqttUsername = data['mqttUsername'],
        mqttPassword = data['mqttPassword'],
        mqttRate = data['mqttRate'],
    )
    return html