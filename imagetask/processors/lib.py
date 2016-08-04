from pilkit import processors
from imagetask.processors.base import recreate_for_spec


Adjust = recreate_for_spec(processors.base.Adjust)
Reflection = recreate_for_spec(processors.base.Reflection)
Transpose = recreate_for_spec(processors.base.Transpose)
MakeOpaque = recreate_for_spec(processors.base.MakeOpaque)
TrimBorderColor = recreate_for_spec(processors.crop.TrimBorderColor)
Crop = recreate_for_spec(processors.crop.Crop)
SmartCrop = recreate_for_spec(processors.crop.SmartCrop)
Resize = recreate_for_spec(processors.resize.Resize)
ResizeToCover = recreate_for_spec(processors.resize.ResizeToCover)
ResizeToFill = recreate_for_spec(processors.resize.ResizeToFill)
SmartResize = recreate_for_spec(processors.resize.SmartResize)
ResizeCanvas = recreate_for_spec(processors.resize.ResizeCanvas)
AddBorder = recreate_for_spec(processors.resize.AddBorder)
ResizeToFit = recreate_for_spec(processors.resize.ResizeToFit)
Thumbnail = recreate_for_spec(processors.resize.Thumbnail)
