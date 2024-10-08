import redis from "redis";
const client = redis
  .createClient()
  .on("error", (error) => {
    console.log(`Redis client not connected to the server: ${error}`);
  })
  .on("connect", () => {
    console.log("Redis client connected to the server");
  });
function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}
async function displaySchoolValue(schoolName) {
    await client.get(schoolName, (error, reply) => {
        if (error) {
            throw error;
        }
        else {
            console.log(reply);
        }
    });
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');