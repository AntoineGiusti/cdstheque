import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CdDetailComponent } from './cd-detail.component';

describe('CdDetailComponent', () => {
  let component: CdDetailComponent;
  let fixture: ComponentFixture<CdDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CdDetailComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CdDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
