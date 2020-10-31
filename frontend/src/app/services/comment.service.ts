import { Injectable } from '@angular/core';
import {Observable} from 'rxjs';
import {CommentPage} from '../commentPage';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Comment} from '../comment';

@Injectable({
  providedIn: 'root'
})
export class CommentService {
  constructor(private http: HttpClient) { }
  private BASE_URL = 'http://localhost:8000/api/comments/';
  httpOptions = {
    headers: new HttpHeaders({ 'Content-Type': 'application/json' })
  };
  getComments(id: number): Observable<any> {
    const url = `${this.BASE_URL}${id}/`;
    return this.http.get(url, this.httpOptions);
  }
  writeComment(message: string, id: number): void {
    const url = `${this.BASE_URL}${id}/post/`;
    this.http.post(url, JSON.stringify(message), this.httpOptions).subscribe(
      data => {
        console.log('oof');
      },
      error => {
        console.log(error);
      }
    );
  }
  updateComment(id: number, delta: number): void {
    const url = this.BASE_URL + 'change/' + id;

    this.http.put(url, JSON.stringify(delta), this.httpOptions).subscribe(
      data => {
        console.log('woof');
        window.location.reload();
      },
      error => {
        console.log(error);
      }
    );
  }
  deleteComment(id: number): void {
    const url = this.BASE_URL + 'delete/' + id;
    this.http.delete(url, this.httpOptions).subscribe(
      data => {
        console.log('woof');
        window.location.reload();
      },
      error => {
        console.log(error);
      }
    );
  }

}
