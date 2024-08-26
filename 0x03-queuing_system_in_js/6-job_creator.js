import kue from "kue";
const queue = kue.createQueue();
queue.on("error", (error) => {
  console.log(error);
});
const job = {
  phoneNumber: 'string',
  message: 'string',
};
const push_notification_code = queue
  .createJob("push_notification_code", job)
  .priority("high")
  .attempts(5)
  .save((error) => {
    if (error) {
      throw error;
    } else {
      console.log(`Notification job created: ${push_notification_code.id}`);
    }
  });
push_notification_code
  .on("complete", (result) => {
    console.log("Notification job completed");
  })
  .on("failed", (errorMessage) => {
    console.log("Notification job failed");
  });
