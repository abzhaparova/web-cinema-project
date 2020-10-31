import { Component, OnInit } from '@angular/core';
import { MatDialog, MatDialogConfig } from '@angular/material/dialog';
import {AuthorizationComponent} from '../authorization/authorization.component';
import {RegistrationComponent} from '../registration/registration.component';
import {TokenStorageService} from '../../services/token-storage.service';
import {Router} from '@angular/router';

@Component({
  selector: 'app-navigation-bar',
  templateUrl: './navigation-bar.component.html',
  styleUrls: ['./navigation-bar.component.css']
})
export class NavigationBarComponent implements OnInit {
  constructor(private matDialog: MatDialog, private tokenStorageService: TokenStorageService,
              private router: Router) { }

  text: string;

  ngOnInit(): void {
    if (this.tokenStorageService.getToken() === null) {
      this.text = 'Log In';
    } else {
      this.text = 'Log Out';
    }
  }

  decide(): void {
    if (this.text === 'Log In') {
      this.login();
    } else {
      this.logout();
    }
  }

  login(): void {
    const dialogConfig = new MatDialogConfig();
    dialogConfig.height = '400px';
    dialogConfig.width = '550px';
    dialogConfig.backdropClass = 'dark-backdrop';
    const modalDialog = this.matDialog.open(AuthorizationComponent, dialogConfig);
  }

  logout(): void {
    this.tokenStorageService.signOut();
    window.location.reload();
  }

  register(): void {
    const dialogConfig = new MatDialogConfig();
    dialogConfig.height = '600px';
    dialogConfig.width = '550px';
    dialogConfig.backdropClass = 'dark-backdrop';
    const modalDialog = this.matDialog.open(RegistrationComponent, dialogConfig);
  }

  profile(): void {
    if (this.tokenStorageService.getToken() === null) {
      alert('You need to login first to view your profile');
    } else {
      this.router.navigate(['/profile/', this.tokenStorageService.getUser()]).then(
        nav => {
          console.log(nav);
        },
        err => {
          console.log(err);
        }
      );
    }
  }
}
