import kue from "kue";
import createPushNotificationsJobs from "./8-job.js";
import chai from "chai";
const expect = chai.expect;
const queue = kue.createQueue();

describe("Tests the createPushNotificationsJobs function", function () {
  let list = [
    {
      phoneNumber: "4153518780",
      message: "This is the code 1234 to verify your account",
    },
  ];

  before(function () {
    queue.testMode.enter();
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function () {
    queue.testMode.exit();
  });

  it("should create a push notification job", function () {
    createPushNotificationsJobs(list, queue);
    const jobs = queue.testMode.jobs;
    expect(jobs).to.have.lengthOf(1);
    const job = jobs[0];
    expect(job.type).to.equal("push_notification_code_3");
    expect(job.data).to.eql({
      phoneNumber: "4153518780",
      message: "This is the code 1234 to verify your account",
    });
  });
});
