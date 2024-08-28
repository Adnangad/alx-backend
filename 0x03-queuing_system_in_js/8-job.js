function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error("Jobs is not an array");
  }
  for (let job of jobs) {
    let push_notification_code_3 = queue
      .create("push_notification_code_3", job)
      .save((error) => {
        if (error) {
          throw error;
        } else {
          console.log(
            `Notification job created: ${push_notification_code_3.id}`
          );
        }
      });
    push_notification_code_3
      .on("complete", (result) => {
        console.log(
          `Notification job ${push_notification_code_3.id} completed`
        );
      })
      .on("failed", (errorMessage) => {
        console.log(
          `Notification job ${push_notification_code_3.id} failed: ${errorMessage}`
        );
      })
      .on("progress", (progress, data) => {
        console.log(
          `Notification job ${push_notification_code_3.id} ${progress}% complete`
        );
      });
  }
}

module.exports = createPushNotificationsJobs;
