import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName, lastName, fileName) {
  const promise1 = {
    status: 'pending ',
  };
  const promise2 = {
    status: 'pending ',
  };

  try {
    const upload = await uploadPhoto(fileName);
    promise2.value = upload;
    promise2.status = 'fulfilled';
  } catch (err) {
    promise2.value = err.toString();
    promise2.status = 'rejected';
  }

  try {
    const signup = await signUpUser(firstName, lastName);
    promise1.value = signup;
    promise1.status = 'fulfilled';
  } catch (err) {
    promise1.value = err.toString();
    promise1.status = 'rejected';
  }

  return [promise1, promise2];
}

export default handleProfileSignup;
