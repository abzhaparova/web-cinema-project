import { Component, OnInit } from '@angular/core';
import {MatDialogRef} from '@angular/material/dialog';
import {AuthenticationService} from '../../services/authentication.service';
import {User} from '../../user';
import {TokenStorageService} from '../../services/token-storage.service';

@Component({
  selector: 'app-authorization',
  templateUrl: './authorization.component.html',
  styleUrls: ['./authorization.component.css']
})
export class AuthorizationComponent implements OnInit {
  username: string;
  password: string;
  message: string;

  constructor(private dialogRef: MatDialogRef<AuthorizationComponent>, private tokenStorageService: TokenStorageService,
              private authenticationService: AuthenticationService) { }

  ngOnInit(): void {
  }
  enter(): void {
    const user = {
      username: this.username,
      password: this.password,
    };
    this.authenticationService.login(user).subscribe(
      data => {
        this.tokenStorageService.saveToken(data.access);
        console.log(data.username);
        this.tokenStorageService.saveUser(user.username);
        window.location.reload();
        this.dialogRef.close();
      },
      error => {
        console.log(error);
        this.message = 'Invalid credentials';
      }
    );
  }
}
