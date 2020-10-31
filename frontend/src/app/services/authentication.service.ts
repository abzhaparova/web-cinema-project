import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import {User} from '../user';


const BASE_URL = 'http://localhost:8000/api/';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' })
};

@Injectable({
  providedIn: 'root'
})



export class AuthenticationService {

  constructor(private http: HttpClient) { }

  login(credentials): Observable<any> {
    return this.http.post(BASE_URL + 'token/obtain/', JSON.stringify(credentials), httpOptions);
  }

  register(user: User): Observable<any> {
    console.log(JSON.stringify(user));
    return this.http.post(BASE_URL + 'user/create/', JSON.stringify(user), httpOptions);
  }

}
