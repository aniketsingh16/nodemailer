import nodemailer from "nodemailer";

const email = 'rockaniket99@gmail.com';
const pass = 'vxzygvbyqtjkyppb'

export const transporter = nodemailer.createTransport({
  service: "gmail",
  auth: {
    user: email,
    pass,
  },
});

export const mailOptions = {
  from: email,
  to: email,
};
