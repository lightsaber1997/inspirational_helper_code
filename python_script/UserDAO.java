package com.inspirational.subject;

import java.util.List;

import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Repository;

@Repository
public interface SubjectDAO {
	public List<Subject> selectAll();
	public Subject selectById(
			@Param("id") int id);
	public Subject selectBySubjectName(
			@Param("subjectName") String subjectName);
}
