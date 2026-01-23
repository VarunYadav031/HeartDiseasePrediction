const { spawn } = require('child_process');
const path = require('path');

exports.handler = async (event, context) => {
  if (event.httpMethod !== 'POST') {
    return {
      statusCode: 405,
      body: JSON.stringify({ error: 'Method not allowed' })
    };
  }

  try {
    const body = JSON.parse(event.body);
    
    // Call your Python prediction script
    const pythonProcess = spawn('python', [
      path.join(__dirname, '../../predict_api.py'),
      JSON.stringify(body)
    ]);

    return new Promise((resolve, reject) => {
      let result = '';
      let error = '';

      pythonProcess.stdout.on('data', (data) => {
        result += data.toString();
      });

      pythonProcess.stderr.on('data', (data) => {
        error += data.toString();
      });

      pythonProcess.on('close', (code) => {
        if (code !== 0) {
          resolve({
            statusCode: 500,
            body: JSON.stringify({ error: error })
          });
        } else {
          resolve({
            statusCode: 200,
            headers: { 'Content-Type': 'application/json' },
            body: result
          });
        }
      });
    });
  } catch (error) {
    return {
      statusCode: 400,
      body: JSON.stringify({ error: error.message })
    };
  }
};
