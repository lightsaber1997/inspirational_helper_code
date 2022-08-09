package com.inspirational.user;

import java.util.List;

import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Repository;

@Repository
public interface UserDAO {
	public List<User> selectUserList();
	public User selectUserById(
			@Param("id") int id);
	public User selectUserByLoginId(
			@Param("loginId") String loginId);
	public User selectUserByUserNameInApp(
			@Param("userNameInApp") String userNameInApp);
	public void insertUser(
			@Param("loginId") String loginId,
			@Param("encryptedPassword") String encryptedPassword,
			@Param("email") String email,
			@Param("phoneNumber") String phoneNumber,
			@Param("authority") String authority,
			@Param("userNameInApp") String userNameInApp,
			@Param("realName") String realName
			);
}
