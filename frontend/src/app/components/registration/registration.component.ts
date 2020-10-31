import { Component, OnInit } from '@angular/core';
import { MovieService } from '../../services/movie.service';
import { MatDialogRef } from '@angular/material/dialog';
import {AuthenticationService} from '../../services/authentication.service';
import {User} from '../../user';

@Component({
  selector: 'app-registration',
  templateUrl: './registration.component.html',
  styleUrls: ['./registration.component.css']
})
export class RegistrationComponent implements OnInit {
  email: string;
  username: string;
  password: string;
  passwordConfirmation: string;
  constructor(private dialogRef: MatDialogRef<RegistrationComponent>, private authenticationService: AuthenticationService) { }

  ngOnInit(): void {
  }
  register(): void {
    if (this.password !== this.passwordConfirmation) {
      return;
    }
    const user: User = {
      username: this.username,
      password: this.password,
      email: this.email
    };
    this.authenticationService.register(user).subscribe(
      data => {
        console.log(data);
      },
      error => {
        console.log(error);
      }
    );
    this.dialogRef.close();
  }

}
