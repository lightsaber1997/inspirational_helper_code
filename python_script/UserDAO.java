package com.inspirational.lessonRequest;

import java.util.List;

import org.apache.ibatis.annotations.Param;

public interface LessonRequestLocationDAO {
	public List<LessonRequest> selectAll();
	public LessonRequest selectById(
			@Param("id") int id);
	public LessonRequest selectByLessonRequestId(
			@Param("lessonRequestId") int lessonRequestId);
	public LessonRequest selectByLocationId(
			@Param("locationId") int locationId);
	public LessonRequest selectByLessonRequestIdAndLocationId(
			@Param("lessonRequestId") int lessonRequestId,
			@Param("locationId") int locationId);
	public void insert(
			@Param("lessonRequestId") int lessonRequestId,
			@Param("locationId") int locationId);
}
