////////////////////////////////////////////////////////////////////////////////
// windowlist.m
// Mark Setchell
//
// Get list of windows with their characteristics
//
// Compile with:
// clang windowlist.m -o windowlist -framework coregraphics -framework cocoa
//
// Run with:
// ./windowlist
//
////////////////////////////////////////////////////////////////////////////////
#include <Cocoa/Cocoa.h>
#include <CoreGraphics/CGWindow.h>

int main(int argc, char **argv)
{
   NSArray *windows = (NSArray *)CGWindowListCopyWindowInfo(kCGWindowListOptionOnScreenOnly,kCGNullWindowID);
   for(NSDictionary *window in windows){
      int WindowNum = [[window objectForKey:(NSString *)kCGWindowNumber] intValue];
      NSString* OwnerName = [window objectForKey:(NSString *)kCGWindowOwnerName];
      int OwnerPID = [[window objectForKey:(NSString *) kCGWindowOwnerPID] intValue];
      NSString* WindowName= [window objectForKey:(NSString *)kCGWindowName];
      CFDictionaryRef bounds = (CFDictionaryRef)[window objectForKey:(NSString *)kCGWindowBounds];
      CGRect rect;
      CGRectMakeWithDictionaryRepresentation(bounds,&rect);
      printf("%s:%s:%d:%d:%f,%f,%f,%f\n",[OwnerName UTF8String],[WindowName UTF8String],WindowNum,OwnerPID,rect.origin.x,rect.origin.y,rect.size.height,rect.size.width);
   }
}