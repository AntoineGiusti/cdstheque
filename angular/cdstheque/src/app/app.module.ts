import { NgModule } from '@angular/core';
import { NgbModule, NgbModalModule } from '@ng-bootstrap/ng-bootstrap';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { AppComponent } from './app.component';
import { CdDetailComponent } from './cd-detail/cd-detail.component';
import { CdsComponent } from './cds/cds.component';
import { MessagesComponent } from './messages/messages.component';
import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { CdSearchComponent } from './cd-search/cd-search.component';
import { DeleteModalComponent } from './delete-modal/delete-modal.component';

@NgModule({

  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule,
    NgbModule,
    NgbModalModule
  ],
  declarations: [
    AppComponent,
    CdsComponent,
    CdDetailComponent,
    MessagesComponent,
    CdSearchComponent,
    DeleteModalComponent,
  ],
  providers: [],
  bootstrap: [AppComponent]

})
export class AppModule { }
